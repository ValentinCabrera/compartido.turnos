
import './App.css';
import Registro from "./rutas/registro/index.jsx"
import Login from "./rutas/login/login.jsx"
import CheckLogin from "./componentes/loginverificado.jsx"
import {
  createBrowserRouter,
  RouterProvider,
} from "react-router-dom";


const router = createBrowserRouter([
  {
    path: "/",
    element: <div>Hello world!</div>,
  },{
    path:"/registro",
    element: <Registro />

  },{
    path:"/login",
    element: <Login />
  },
  {
    path:"/checklogin/:token",
    element: <CheckLogin />
  }
]);


function App() {
  return (
    <RouterProvider router={router} />
  );
}

export default App;
