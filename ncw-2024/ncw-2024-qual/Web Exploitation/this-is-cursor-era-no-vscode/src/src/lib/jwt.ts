import jwt from 'jsonwebtoken'

const secret = process.env.APP_SECRET as string
console.log(secret)

export const createJWT = (payload: any) => {
	return jwt.sign(payload, secret)
}

export const verifyJWT = (token: string) => {
	return jwt.verify(token, secret)
}
