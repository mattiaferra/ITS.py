import React from 'react'

const Clock = (props) => {
    const t=Date.now()+3600*props.timezone*1000;
    const date=new Date(t)
  return (
    <h3>In {props.country}  sono le {date.toLocaleDateString()} del giorno {date.toLocaleTimeString()}</h3>
    
  )
}

export default Clock