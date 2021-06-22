import React from 'react'
import { Text } from 'react-native'
import Estilo from './estilo'


export default props => { 
                      
    const {min, max} = props
    const num = Math.random() * (max - min) + min
    const numInt = parseInt(num)

    return (
        <Text style={Estilo.txtG}>
            Um valor entre { max } e { min } é {numInt}
        </Text>
    )
}