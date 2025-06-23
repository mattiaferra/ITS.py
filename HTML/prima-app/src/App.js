import './App.css';
import Clock from './Clock';
import Componente1 from './Componente1';
import Stampanumeri from './Esercizi/Stampa_numeri';
import Tabellinacinque from './Esercizi/Tabellinacinque';

//function getDate(date){
  //return date.toLocaleDateString()+" "+date.toLocaleTimeString()
//}

function App() {
  return (
    <div className="App">
      <Stampanumeri></Stampanumeri>
      <Tabellinacinque numero="5"></Tabellinacinque>
      <h1>Primo Elemento</h1>
       <Componente1>Mattia</Componente1>
       <Componente1/>
      <h2>
        {
          new Date().toLocaleDateString()+" "+new Date().toLocaleTimeString()
        }
        
      </h2>
      <Clock timezone="0" country ="Italy"></Clock>
      <Clock timezone="6" country ="USA"></Clock>
      <Clock timezone="8" country ="Japan"></Clock>


    </div>
  );
}

export default App;
