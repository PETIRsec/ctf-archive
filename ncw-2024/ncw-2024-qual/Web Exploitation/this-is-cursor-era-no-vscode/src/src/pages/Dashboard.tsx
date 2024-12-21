import { FC } from 'hono/jsx'
import Layout from './Layout'
import { User } from '../lib/types'

const Dashboard: FC<{ user: User }> = ({ user }) => {
	return (
		<Layout>
			<h1>Dashboard</h1>
			<p>Your user data:</p>
			<pre>{JSON.stringify(user, null, 2)}</pre>
			<h2>AI Chat</h2>
			<img src='/static/ai.png' />
			<p>Coming soon... (not really, malas bikin ui nya ehe)</p>
		</Layout>
	)
}

export default Dashboard
