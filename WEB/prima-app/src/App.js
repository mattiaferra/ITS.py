import './App.css';
import { useState } from 'react';
import Clock from './Clock';
import Componente1 from './Componente1';
import EsempioUseEffect from './EsempioUseEffect';
import Contatore from './Contatore';
import Stampanumeri from './Esercizi/Stampa_numeri';
import Tabellinacinque from './Esercizi/Tabellinacinque';
import CambiaNome from './Esercizi/CambiaNome';
import LoginForm from './Esercizi/LoginForm';
import { anagrafica } from "./data/dati";
import FetchComponent from './FetchComponent';



function App() {
  const [nome1, setNome1] = useState("nome");
  const [persone, setPersone] = useState(anagrafica);
/*
  const cambiaNome = () => {
    const nuovoNome = "Mario";
    setNome1(nuovoNome);
  };*/


  const cambiaNome = () => {
    const nuovoNome = "Mattia";
    setNome1(nuovoNome);
  }



  const cliccami = (nome, cognome) => {
    alert("Ciao " + nome + " " + cognome);
  };

  const elimina = (id) => {
    const newAnag = persone.filter((p) => p.id !== id);
    setPersone(newAnag);
  };

  const [persona,setPersona]=useState({

    id:"1",
    nome:"Rob",
    cognome:"Del",
    eta:48
  })

  const compleanno=()=>{
    let anni = persona.eta+1;

    setPersona({

      ...persona,
      eta:anni
    })


  }



  return (
    <div className="App">
      {/* 
      <Stampanumeri />
      <Tabellinacinque numero="5" />
      <h1>Primo Elemento</h1>
      <Componente1>Mattia</Componente1>
      <Componente1 />
      <h2>
        {new Date().toLocaleDateString() + " " + new Date().toLocaleTimeString()}
      </h2>
      <Clock timezone="0" country="Italy" />
      <Clock timezone="6" country="USA" />
      <Clock timezone="8" country="Japan" />
      */}
      <FetchComponent></FetchComponent>
      <LoginForm></LoginForm>
      <CambiaNome></CambiaNome>
      <EsempioUseEffect></EsempioUseEffect>
      <Contatore></Contatore>

      <h1>{nome1}</h1>
      <button onClick={cambiaNome} className="btn btn-primary">
        Cambia Nome
      </button>


<br></br>
<br></br>
<div>{persona.nome}</div>
<div>{persona.cognome}</div>
<div>{persona.eta}</div>
<button onClick={compleanno} className="btn btn-primary">
Compleanno    </button>
  

  

      {persone.map((p) => (
        <div key={p.id}>
          <span>{p.nome} {p.cognome}</span>&nbsp;
          <button onClick={() => elimina(p.id)}>Elimina</button>
        </div>
      ))}
    </div>
  );
}

export default App;