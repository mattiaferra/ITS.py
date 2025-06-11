const rootElement= document.querySelector("#root");


const root=ReactDOM.createRoot(rootElement);




const App= (props)=>{
    return(
        <main ClassName="main">
            <h1>Primo Componente</h1>
            
        </main>
    )
}
const List=()=>{

    return(
        <ul>
            <li>Php</li> 
            <li>JS</li>
            <li>Python</li>
        </ul>
    )
}
é
root.render(

<>

    <App>
        <h2>Lista Competenze</h2>
        <List></List>
    </App>

</>    
)