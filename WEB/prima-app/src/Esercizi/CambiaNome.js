
import { useState } from "react";

const CambiaNome = () => {
  const [nome, setNome] = useState("Mattia :)");

  const cambia = () => {
    if (nome === "Mattia :)") {
      setNome("Mario");
    } else {
      setNome("Mattia :)");
    }
  };

  return (
    <div>
      <h3>{nome}</h3>
      <button className="btn btn-dark" onClick={cambia}>
        Cambia Nome
      </button>
    </div>
  );
};

export default CambiaNome;
