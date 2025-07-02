import React from 'react'

const numeri  = [1,2,3,4,5,6,7,8,9,10]



const Stampanumeri = () => {
  return (
    <div>{numeri.map((n)=>{return <p>{n}</p>})}</div>
  )

}

export default Stampanumeri