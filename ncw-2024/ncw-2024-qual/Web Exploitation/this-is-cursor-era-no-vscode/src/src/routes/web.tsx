import { Hono } from 'hono'
import { Variables } from '../lib/session'
import { authMiddleware } from '../lib/middlewares'
import Login from '../pages/Login'
import Register from '../pages/Register'
import Dashboard from '../pages/Dashboard'

const web = new Hono<{
	Variables: Variables
}>()

web.get('/', (c) => {
	return c.redirect('/login')
})
web.get('/login', (c) => {
	return c.html(<Login />)
})
web.get('/register', (c) => {
	return c.html(<Register />)
})
web.get('/dashboard', authMiddleware, (c) => {
	let user = c.get('user')
	return c.html(<Dashboard user={user} />)
})

export default web
