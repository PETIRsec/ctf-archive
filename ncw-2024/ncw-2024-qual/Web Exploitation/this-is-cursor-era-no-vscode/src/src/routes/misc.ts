import { Hono } from 'hono'
import { Variables } from '../lib/session'
import { authMiddleware } from '../lib/middlewares'
import sql, { getSession } from '../lib/db'

const misc = new Hono<{
	Variables: Variables
}>()

misc.put('/add-balance', authMiddleware, async (c) => {
	let user = c.get('user')
	let sessionData = await getSession(user.sessionId)

	if (sessionData.balance != 0) {
		return c.json({ message: 'Jangan maruk bang' }, 403)
	}

	await sql`UPDATE sessions SET balance = balance + 999 WHERE session_id = ${user.sessionId}`

	return c.json({ message: 'Balance added' }, 200)
})

misc.put('/remove-trust-issue', authMiddleware, async (c) => {
	let user = c.get('user')
	let sessionData = await getSession(user.sessionId)

	if (user.role !== 'admin' || !sessionData.is_trust_issue) {
		return c.json({ message: 'Nu uh' }, 403)
	}

	if (sessionData.balance < 1000) {
		return c.json({ message: 'Nu uh' }, 400)
	}

	await sql`UPDATE sessions SET is_trust_issue = FALSE WHERE session_id = ${user.sessionId}`

	return c.json({ message: 'Trust issue removed' }, 200)
})

misc.get('/me', authMiddleware, (c) => {
	let user = c.get('user')
	return c.json({ user }, 200)
})

export default misc
