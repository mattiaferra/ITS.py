import React from 'react'
import { useNavigate } from 'react-router-dom'

const ErrorPage = () => {
    const navigate = useNavigate ()
  return (
    <>
    <div>Pagina non trovata</div>
    <div><button className = 'btn' onClick = {() => navigate("/")}>Torna alla Home</button></div>
    <hr></hr>
    <div><button className = 'btn' onClick = {() => navigate(-1)}>Torna alla pagina precedente</button></div>
    </>
  );
};

export default ErrorPage;