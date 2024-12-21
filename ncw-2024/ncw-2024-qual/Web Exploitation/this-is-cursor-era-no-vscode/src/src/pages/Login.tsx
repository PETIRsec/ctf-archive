import { FC } from 'hono/jsx'
import { css } from 'hono/css'
import Layout from './Layout'

const Login: FC = () => {
	return (
		<Layout>
			<h1
				class={css`
					font-size: 2rem;
					font-weight: 700;
					margin-bottom: 1rem;
				`}
			>
				Login
			</h1>
			<form
				action='/api/auth/login'
				class={css`
					display: flex;
					flex-direction: column;
					gap: 1rem;
					max-width: 300px;
					margin: 0 auto;
				`}
			>
				<input
					type='text'
					name='username'
					placeholder='Username'
					class={css`
						padding: 0.5rem;
						border: 1px solid #ccc;
						border-radius: 4px;
					`}
				/>
				<input
					type='password'
					name='password'
					placeholder='Password'
					class={css`
						padding: 0.5rem;
						border: 1px solid #ccc;
						border-radius: 4px;
					`}
				/>
				<button
					type='submit'
					class={css`
						padding: 0.5rem 1rem;
						background-color: #007bff;
						color: white;
						border: none;
						border-radius: 4px;
						cursor: pointer;
						&:hover {
							background-color: #0056b3;
						}
					`}
				>
					Log In
				</button>
			</form>
			<p
				class={css`
					margin-top: 1rem;
					text-align: center;
				`}
			>
				Don't have an account?{' '}
				<a
					href='/register'
					class={css`
						color: #007bff;
						text-decoration: none;
						&:hover {
							text-decoration: underline;
						}
					`}
				>
					Register here
				</a>
			</p>
		</Layout>
	)
}

export default Login
