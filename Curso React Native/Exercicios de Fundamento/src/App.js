import React from 'react'
import { SafeAreaView, StyleSheet } from 'react-native'

import Mega from './components/mega/Mega'
// import ListaProdutos from './components/produtos/ListaProdutos'
// import UsuarioLogado from './components/UsuarioLogado'
// import Familia from './components/relacao/Familia'
// import Membro from './components/relacao/Membro'
// import ParImpar from './components/ParImpar'
// import ContadorV2 from './components/contador/ContadorV2'
// import Pai from './components/indireta/Pai'
// import Pai from './components/direta/Pai'
// import Contador from './components/Contador'
// import Botao from './components/Botao'
// import Titulo from './components/Titulo'
// import Aleatorio from './components/Aleatorio' 
// import MiMax from './components/MiMax'
// import CompPadrao, { Comp1, Comp2 } from './components/Multi'
// import Primeiro from './components/Primeiro'

export default () => (
    <SafeAreaView style={style.App}> 
        <Mega qtdeNumeros = {1} />
        {/*
        <ListaProdutos />
        <UsuarioLogado usuario={{ nome:'Thiago', email:'thiago@thiago.com' }}/>
        <UsuarioLogado usuario={{ nome:'Joao'}}/>
        <UsuarioLogado usuario={{ email:'maria@maria.com' }}/>
        <Familia>
            <Membro nome ="João" sobrenome = "Ferreira" />
            <Membro nome ="Maria" sobrenome = "Ferreira" />
        </Familia>
        <Familia>
            <Membro nome ="Petrucio" sobrenome = "Amorim" />
            <Membro nome ="Beatriz" sobrenome = "Amorim" />
        </Familia>
        <ParImpar num={3}/>
        <ContadorV2 />
        <Pai />
        <Pai />
        <Contador inicial={100} passo={13}/>
        <Botao />
        <Titulo principal="Cadastro Produto" secundario="Tela de Cadastro do Produto" />
        <Aleatorio min= {1} max = {20}/>
        <MiMax min="3" max="20" />
        <CompPadrao />
        <Comp1 />
        <Comp2 />
        <Primeiro /> 
        */}
    </SafeAreaView>
)

const style = StyleSheet.create({
    App: {
        flexGrow: 1, 
        justifyContent: "center",
        alignItems: "center",
        padding: 20
    }
})