const express = require('express');
const router = express.Router();
const DOMPurify = require('isomorphic-dompurify');
const { fork } = require('child_process');
const JWTHelper = require('../helpers/JWTHelper');
const { getUserByUsername, createUser, updateUserProfile, getAllUsers, getUserById, updateUserDetails } = require('../helpers/database');
const { merge } = require('../helpers/merge');
const { authMiddleware } = require('../middleware/AuthMiddleware');
const routeCache = require('route-cache');
const { visitPost } = require('../bot')

let botVisiting = false;

const cacheKey = (req, res) => {
    return `_${req.url}_${(req.headers['x-forwarded-for'] || req.ip)}`;
}

router.get('/', (req, res) => {
    res.render('index.html', { user: req.user });
});

router.get('/home', authMiddleware, (req, res) => {
    res.render('home.html', { user: req.user });
});

router.get('/register', (req, res) => {
    res.render('register.html');
});

router.post('/register', async (req, res) => {
    try {
        const { username, password } = req.body;

        getUserByUsername(username, (err, user) => {
            if (err) {
                return res.status(500).send('Database error');
            }

            if (user) {
                return res.status(400).send('Username already taken. Please choose a different one.');
            } 

            createUser(username, password, 'https://avatar.iran.liara.run/public', 'user', (err) => {
                if (err) {
                    return res.status(500).send('Error registering user');
                }
                res.redirect('/login');
            });
        });
    } catch (error) {
        console.error(error);
        res.status(500).send('An unexpected error occurred.');
    }
});

router.get('/login', (req, res) => {
    res.render('login.html');
});

router.post('/login', async (req, res) => {
    try {
        const { username, password } = req.body;

        getUserByUsername(username, (err, user) => {
            if (err) {
                return res.status(500).send('Database error');
            }

            if (!user || (password !== user.password)) {
                return res.status(400).send('Invalid credentials');
            } else {
                const token = JWTHelper.sign({ id: user.id, username: user.username, profile_pic: user.profile_pic, role: user.role });
                res.cookie('session', token);
                res.redirect('/home');
            }
        });
    } catch (error) {
        console.error(error);
        res.status(500).send('An unexpected error occurred.');
    }
});


router.get('/profile', authMiddleware, routeCache.cacheSeconds(15, cacheKey), async (req, res) => {
    res.render('profile.html', { user: await req.user });
});

router.post('/profile', authMiddleware, async (req, res) => {
    try {
        const { profile_pic } = req.body;
        const userId = req.user.id;

        if (!profile_pic) {
            return res.status(400).send('All fields (username, profile picture, password) are required.');
        }

        const sanitizedURL = DOMPurify.sanitize(profile_pic);

        updateUserProfile(userId, sanitizedURL, (err) => {
            if (err) {
                return res.status(500).send('An error occurred while updating your profile.');
            }
            getUserByUsername(req.user.username, (err, user) => {
                if (err) {
                    return res.status(500).send('Database error');
                }
                const token = JWTHelper.sign({ id: user.id, username: user.username, profile_pic: user.profile_pic, role: user.role });
                res.cookie('session', token);
                res.status(200).send('Profile updated successfully.');
            });
        });
    } catch (error) {
        console.error(error);
        res.status(500).send('An unexpected error occurred.');
    }
});

router.get('/logout', (req, res) => {
    res.clearCookie('session');
    res.redirect('/');
});

router.get('/manage', authMiddleware, async (req, res) => {
    try {
        if (req.user.role !== 'admin') return res.status(403).send('Forbidden');

        getAllUsers((err, rows) => {
            if (err) {
                return res.status(500).send('Database error');
            }
            res.render('manage.html', { users: rows });
        });
    } catch (error) {
        console.error(error);
        res.status(500).send('An unexpected error occurred.');
    }
});

router.get('/manage/:id', authMiddleware, async (req, res) => {
    try {
        if (req.user.role !== 'admin') return res.status(403).send('Forbidden');

        getUserById(req.params.id, (err, row) => {
            if (err) {
                return res.status(500).send('Database error');
            }
            res.render('manage-user.html', { user: row });
        });
    } catch (error) {
        console.error(error);
        res.status(500).send('An unexpected error occurred.');
    }
});

router.post('/manage/:id', authMiddleware, async (req, res) => {
    try {
        if (req.user.role !== 'admin') return res.status(403).send('Forbidden');

        const updatedUser = req.body;
            updateUserDetails(req.params.id, updatedUser.username, updatedUser.profile_pic, updatedUser.password, (err) => {
            if (err) {
                return res.status(500).send('Database error');
            }

            let userData = {};
            userData = merge(userData, updatedUser);

            const child = fork('./log.js');
            child.send(userData);

            res.send('User updated');
        });
    } catch (error) {
        console.error(error);
        res.status(500).send('An unexpected error occurred.');
    }
});

router.get('/report', (req, res) => {
    res.render('report.html');
});

router.post('/report', async (req, res) => {
    const {
        url
    } = req.body;

    var pattern = /^((http|https):\/\/)/;

    if(!pattern.test(url)) {
        return res.status(400).send('URL Malformed');
    }

    if (botVisiting) return res.status(403).send('Please wait for the previous report to process first!');
    if (url) {
        botVisiting = true;
        return visitPost(url)
            .then(() => {
                botVisiting = false;
                return res.send('Report received successfully!');
            })
            .catch(e => {
                console.error(e)
                botVisiting = false;
                return res.status(403).send('Something went wrong, please try again!');
            })
    }
    return res.status(500).send('Missing required parameters!');
});

module.exports = router;
