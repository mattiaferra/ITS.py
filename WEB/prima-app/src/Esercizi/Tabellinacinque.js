import React from 'react'

const numeri = [1,2,3,4,5,6,7,8,9,10]

const Tabellinacinque = ({numero}) => {
  return (
    <div>Tabbellina del 5{numeri.map((n)=>{return <p>{n*numero}</p>})}</div>
  )
}

export default Tabellinacinque