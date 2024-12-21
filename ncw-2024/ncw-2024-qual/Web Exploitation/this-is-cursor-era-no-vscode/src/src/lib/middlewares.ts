import { Context, Next } from 'hono'
import { Variables } from './session'
import { User } from './types'

export const authMiddleware = async (c: Context<{ Variables: Variables }>, next: Next) => {
	const session = c.get('session')
	const id = session.get('id') as string
	const username = session.get('username') as string
	const role = session.get('role') as string
	const sessionId = session.get('sessionId') as string

	if (!username || !role) {
		return c.json({ message: 'Unauthorized' }, 401)
	}

	const user: User = { id, username, role, sessionId }
	c.set('user', user)

	await next()
}

// Add this to the global Hono type to include the 'user' property
declare module 'hono' {
	interface ContextVariableMap {
		user: User
	}
}
