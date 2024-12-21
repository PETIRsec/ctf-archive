import { CookieStore, Session, sessionMiddleware } from 'hono-sessions'

export type Variables = {
	session: Session
	session_key_rotation: boolean
}

export const createSessionMiddleware = ({ store }: { store: CookieStore }) =>
	sessionMiddleware({
		store,
		encryptionKey: process.env.APP_SECRET,
		cookieOptions: {
			sameSite: 'Lax',
			path: '/',
			httpOnly: true,
		},
	})
