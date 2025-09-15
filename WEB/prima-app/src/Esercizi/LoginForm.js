import { useState } from "react";

const LoginForm = () => {
  const [nome, setNome] = useState("");
  const [cognome, setCognome] = useState("");

  return (
    <div className="container">
      <form className="row g-3">
        <div className="col-md-6">
          <label htmlFor="nome">Nome</label>
          <input
            type="text"
            id="nome"
            className="form-control"
            required
            value={nome}
            onChange={(event) => setNome(event.target.value)}
          />
        </div>
        <div className="col-md-6">
          <label htmlFor="cognome">Cognome</label>
          <input
            type="text"
            id="cognome"
            className="form-control"
            required
            value={cognome}
            onChange={(event) => setCognome(event.target.value)}
          />
        </div>
        <button className="btn btn-success">Login</button>
      </form>
    </div>
  );
};

export default LoginForm;


/*<div>
        <form>
            <div>
                <label>NomeUtente</label>
                <input type="NomeUtente" required></input>
                <label>password</label>
                <input type="password" required value={password} oneChange={(event)=> setPassword(event.target.value)}></input>
            </div>
            <button className="btn btn-success">Login</button>
        </form>
        {NomeUtente} {password}
    </div>)*/