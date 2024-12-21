import 'dotenv/config'
import { serve } from '@hono/node-server'
import { Hono } from 'hono'
import { initDb } from './lib/db'
import auth from './routes/auth'
import chat from './routes/chat'
import web from './routes/web'
import { Variables } from './lib/session'
import { CookieStore, sessionMiddleware } from 'hono-sessions'
import misc from './routes/misc'
import { serveStatic } from '@hono/node-server/serve-static'

initDb()
const app = new Hono<{
	Variables: Variables
}>()

const store = new CookieStore()
app.use(
	'*',
	sessionMiddleware({
		store,
		encryptionKey: process.env.APP_SECRET,
		cookieOptions: {
			sameSite: 'Lax',
			path: '/',
			httpOnly: true,
		},
	})
)

app.get(
	'/static/*',
	serveStatic({
		root: './',
		rewriteRequestPath: (path) => path.replace(/^\/static/, '/statics'),
	})
)

app.route('/', web)
app.route('/api', misc)
app.route('/api/auth', auth)
app.route('/api/chat', chat)

app.notFound((c) => {
	return c.text('Route Not Found :(', 404)
})

app.onError((err, c) => {
	console.error(`${err}`)
	return c.text('Something went wrong', 500)
})

const port = 3000
console.log(`Server is running on port ${port}`)

serve({
	fetch: app.fetch,
	port,
})
