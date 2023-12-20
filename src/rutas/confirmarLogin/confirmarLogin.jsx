import CheckLogin from "../../componentes/loginverificado.jsx"
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
function ConfirmarLogin(){
    return(
        <Router>
        <Routes>
            <Route path="/confirmarlogin/:token" element={<CheckLogin />} />
        </Routes>
    </Router>
    )
}


export default ConfirmarLogin;