import { css, Style } from 'hono/css'
import { FC } from 'hono/jsx'

const Layout: FC = ({ children }) => {
	return (
		<html>
			<Style />
			<body
				class={css`
					margin: 0;
					padding: 0;
					display: flex;
					flex-direction: column;
					align-items: center;
					justify-content: center;
					height: 100vh;
					font-family: 'Inter', sans-serif;
				`}
			>
				{children}
			</body>
		</html>
	)
}

export default Layout
