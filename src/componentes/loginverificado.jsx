import React, { useState } from "react";
import { Form, Button, Alert } from "react-bootstrap";
import 'bootstrap/dist/css/bootstrap.min.css';
import { useParams } from "react-router-dom";
const UrlEndpoint = "http://localhost:8000/auth/check-mail/";
const CheckLogin = () => {
    const [email, setEmail] = useState("");
    const [password, setPassword] = useState("");
    const [error, setError] = useState("");
    const [successMessage, setSuccessMessage] = useState("");
    const { token } = useParams();
    const handleSubmit = async (e) => {
        e.preventDefault();

        try {
            const response = await fetch(UrlEndpoint, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({
                    mail: email,
                    password: password,
                    token: getTokenFromURL(), // Función para obtener el token de la URL
                }),
            });

            const data = await response.json();

            if (!response.ok) {
                setError(data.message || 'Error al verificar el mail');
                setSuccessMessage("");
            } else {
                setError("");
                setSuccessMessage("Verificación de mail exitosa");
                // Aquí podrías guardar el token en el localStorage o en el estado global de tu aplicación
            }
        } catch (error) {
            console.error("Error en la solicitud:", error);
            setError("Error al conectarse al servidor");
            setSuccessMessage("");
        }
    };

    const getTokenFromURL = () => {
        // Lógica para obtener el token de la URL (ejemplo: 'http://localhost:3000/checklogin/DvSLO8F7xWbTzlX70lWvWlCh0yhjgdUcyzXsnSRPJxbA6P8p5N')
        // Puedes implementar la lógica para extraer el token de la URL aquí
        const url = window.location.href;
        const token = url.substring(url.lastIndexOf('/') + 1);
        return token;
    };

    return (
        <div className="container mt-5">
            <h2>Verificar Mail</h2>
            {error && <Alert variant="danger">{error}</Alert>}
            {successMessage && <Alert variant="success">{successMessage}</Alert>}
            <Form onSubmit={handleSubmit}>
                <Form.Group controlId="formEmail">
                    <Form.Label>Email</Form.Label>
                    <Form.Control
                        type="email"
                        placeholder="Ingrese su email"
                        value={email}
                        onChange={(e) => setEmail(e.target.value)}
                        required
                    />
                </Form.Group>

                <Form.Group controlId="formPassword">
                    <Form.Label>Contraseña</Form.Label>
                    <Form.Control
                        type="password"
                        placeholder="Ingrese su contraseña"
                        value={password}
                        onChange={(e) => setPassword(e.target.value)}
                        required
                    />
                </Form.Group>

                <Button variant="primary" type="submit">
                    Verificar Mail
                </Button>
            </Form>
        </div>
    );
}

export default CheckLogin;
