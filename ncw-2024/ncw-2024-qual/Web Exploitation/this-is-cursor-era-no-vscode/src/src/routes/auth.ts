import { Hono } from 'hono'
import sql from '../lib/db'
import { sanitizeUsername } from '../lib/utils'
import crypto from 'crypto'
import { Variables } from '../lib/session'
import { setCookie } from 'hono/cookie'
import { createJWT } from '../lib/jwt'

const auth = new Hono<{
	Variables: Variables
}>()

auth.get('/register', async (c) => {
	let { username, password } = c.req.query()

	if (!username || !password) {
		return c.json({ message: 'Username and password are required' }, 400)
	}

	username = sanitizeUsername(username)
	let account = await sql`SELECT * FROM users WHERE username = ${username}`

	if (account[0]) {
		return c.json({ message: 'Username already taken' }, 400)
	}

	username = username.trim()

	await sql`INSERT INTO users (username, password, role) VALUES (${username}, ${password}, 'user')`

	let sessionKey = crypto.randomUUID()

	await sql`INSERT INTO sessions (session_id, username) VALUES (${sessionKey}, ${username})`

	return c.json({ message: 'Account created successfully', sessionKey }, 201)
})

auth.get('/login', async (c) => {
	let { username, password, sessionKey } = c.req.query()

	if (!username) {
		return c.json({ message: 'Username is required' }, 400)
	}

	let userData
	let sessionData

	if (sessionKey) {
		sessionData = (await sql`SELECT * FROM sessions WHERE session_id = ${sessionKey}`)[0]

		if (!sessionData) {
			return c.json({ message: 'Invalid session key' }, 401)
		}

		userData = (await sql`SELECT * FROM users WHERE username = ${sessionData.username}`)[0]

		if (!userData) {
			return c.json({ message: 'Invalid session key' }, 401)
		}
	} else {
		if (!password) {
			return c.json({ message: 'Password is required' }, 400)
		}

		userData = (await sql`SELECT * FROM users WHERE username = ${username}`)[0]

		if (!userData) {
			return c.json({ message: 'Invalid username or password' }, 401)
		}

		if (userData.password !== password) {
			return c.json({ message: 'Invalid username or password' }, 401)
		}

		sessionData = (await sql`SELECT * FROM sessions WHERE username = ${username}`)[0]

		if (!sessionData) {
			return c.json({ message: 'Invalid session key' }, 401)
		}
	}

	let session = c.get('session')
	session.set('id', userData.id)
	session.set('username', userData.username)
	session.set('role', userData.role)
	session.set('sessionId', sessionData.session_id)
	session.set('balance', sessionData.balance)
	session.set('isTrustIssue', sessionData.is_trust_issue)

	return c.json({ message: 'Login successful' }, 200)
})

export default auth
