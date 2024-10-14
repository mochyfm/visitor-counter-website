import { io } from 'socket.io-client';

// const HOST = import.meta.env.HOST;
// const PORT = import.meta.env.PORT;

const socket = io(`http://${'127.0.0.1'}:${5000}`);

export default socket;
