import { render, screen } from '@testing-library/react';
import {rest} from 'msw';
import App from './App';
import {setupServer} from "msw/node";

const expectedText = 'Text from mock get endpoint';
let handlers = [
  rest.get('http://127.0.0.1:8000/paper/', async (req, res, ctx) => {
    return res(ctx.json([{contents: expectedText}]))
  }),
]

let server = setupServer(...handlers);


beforeAll(() => server.listen())
afterEach(() => server.resetHandlers())
afterAll(() => server.close())


test('shows text from paper', async () => {
  render(<App/>);
  expect(await screen.findByText(expectedText)).toBeInTheDocument()
})