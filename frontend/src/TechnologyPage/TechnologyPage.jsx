import React from 'react';
import config from 'config';
import DataProvider from "../components/DataProvider";
import Table from "../components/Table";
// import Form from "../components/Form";

const TechnologyPage = () => {
    const API_URL = `${config.apiUrl}/technologies/`;

    return <>
        <div className="container">
            <h2>Techonologies</h2>
            <DataProvider endpoint={API_URL} render={data => <Table data={data} />} />
            {/* <Form endpoint={API_URL} /> */}
        </div>
    </>

    // return <>
    //     <div className="container">
    //         <h2>Techonologies</h2>
    //         <p>Carga las tecnologias</p>
    //         <Table striped>
    //             <thead>
    //                 <tr><th>Name</th></tr>
    //             </thead>
    //             <tbody>
    //                 {technologies.map((technology,i) => <tr key={technology.name}><td>{technology.name}</td></tr>) }
    //             </tbody>
    //         </Table>
    //     </div>
    // </>
}

export { TechnologyPage };