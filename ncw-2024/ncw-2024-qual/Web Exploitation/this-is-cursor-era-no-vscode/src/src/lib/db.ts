import postgres from 'postgres'

const sql = postgres(process.env.DATABASE_URL || '')

export default sql

export const initDb = async () => {
	// await sql`DROP TABLE IF EXISTS users`
	// await sql`DROP TABLE IF EXISTS sessions`

	await sql`
        CREATE TABLE IF NOT EXISTS users (
            id SERIAL PRIMARY KEY,
            username VARCHAR(255),
            password VARCHAR(255) NOT NULL,
            role VARCHAR(255) NOT NULL
        );
    `
	await sql`
        CREATE TABLE IF NOT EXISTS sessions (
            id SERIAL PRIMARY KEY,
            session_id VARCHAR(255) UNIQUE NOT NULL,
            username VARCHAR(255) NOT NULL,
            balance INTEGER DEFAULT 0,
            is_trust_issue BOOLEAN DEFAULT TRUE,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
    `

	const adminUser = (
		await sql`
        SELECT * FROM users WHERE username = 'admin';
    `
	)[0]

	if (!adminUser) {
		await sql`
            INSERT INTO users (username, password, role)
            VALUES ('admin', ${process.env.ADMIN_PASSWORD || 'admin'}, 'admin');
        `
		console.log('Admin user created')
	} else {
		console.log('Admin user already exists')
	}

	console.log('Database initialized')
}

export const getSession = async (sessionId: string) => {
	return (await sql`SELECT * FROM sessions WHERE session_id = ${sessionId}`)[0]
}
