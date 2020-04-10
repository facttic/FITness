import React from 'react';
import {Table} from "reactstrap";

const TechnologyPage = () => {
    const technologies = [
        {name: "NodeJs"},
        {name: "Elixir"},
        {name: "Erlang"},
        {name: "Javascript"},
        {name: "Java"},
        {name: "Haskell"},
        {name: "Python"}
    ]


    return <>
        <div className="container">
            <h2>Techonologies</h2>
            <p>Carga las tecnologias</p>
            <Table striped>
                <thead>
                    <tr><th>Name</th></tr>
                </thead>
                <tbody>
                    {technologies.map((technology,i) => <tr><td>{technology.name}</td></tr>) }
                </tbody>
            </Table>
        </div>
    </>
}

export { TechnologyPage };