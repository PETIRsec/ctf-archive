export interface User {
	id: string
	username: string
	role: string
	sessionId: string
}

export interface ChatHistory {
	role: 'system' | 'user' | 'assistant'
	content: string
}
