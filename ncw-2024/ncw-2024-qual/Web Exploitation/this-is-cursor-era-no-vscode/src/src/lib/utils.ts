export const sanitizeUsername = (username: string) => {
	return username.replace(/[!@#$^&*()_+\-=\[\]{};':"\\|,.<>\/? ]/g, '')
}
