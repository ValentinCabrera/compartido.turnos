import React, { useState } from "react";
import { Form, Button } from "react-bootstrap";
import 'bootstrap/dist/css/bootstrap.min.css';

const baseUrl = 'http://localhost:8000';
const signInEndpoint = '/auth/signin/';

const signInUrl = `${baseUrl}${signInEndpoint}`;

const RegistroComponent = () => {
  const [nombre, setNombre] = useState("");
  const [apellido, setApellido] = useState("");
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");

  const handleSubmit = async (e) => {
    e.preventDefault();
    
    try {
      const response = await fetch(signInUrl, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          mail: email,
          name: nombre,
          surname: apellido,
          password: password,
        }),
      });

      if (response.ok) {
        // Aquí puedes manejar la lógica después de un registro exitoso
        console.log('Registro exitoso');
        // Por ejemplo, puedes redirigir a otra página o mostrar un mensaje de éxito
      } else {
        // Manejo de errores en caso de que la solicitud no sea exitosa
        console.error('Error al registrar');
        // Puedes mostrar un mensaje de error o tomar otras acciones necesarias
      }
    } catch (error) {
      console.error('Error:', error);
      // Manejo de errores en caso de una excepción
    }
  };

  return (
    <Form onSubmit={handleSubmit}>
      <Form.Group controlId="formNombre">
        <Form.Label>Nombre</Form.Label>
        <Form.Control
          type="text"
          placeholder="Ingrese su nombre"
          value={nombre}
          onChange={(e) => setNombre(e.target.value)}
        />
      </Form.Group>

      <Form.Group controlId="formApellido">
        <Form.Label>Apellido</Form.Label>
        <Form.Control
          type="text"
          placeholder="Ingrese su apellido"
          value={apellido}
          onChange={(e) => setApellido(e.target.value)}
        />
      </Form.Group>

      <Form.Group controlId="formEmail">
        <Form.Label>Email</Form.Label>
        <Form.Control
          type="email"
          placeholder="Ingrese su email"
          value={email}
          onChange={(e) => setEmail(e.target.value)}
        />
      </Form.Group>

      <Form.Group controlId="formPassword">
        <Form.Label>Contraseña</Form.Label>
        <Form.Control
          type="password"
          placeholder="Ingrese su contraseña"
          value={password}
          onChange={(e) => setPassword(e.target.value)}
        />
      </Form.Group>

      <Button variant="primary" type="submit">
        Registrarse
      </Button>
    </Form>
  );
};

export default RegistroComponent;
