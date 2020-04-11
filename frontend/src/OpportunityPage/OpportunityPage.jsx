import React from 'react';
import config from 'config';
import DataProvider from "../components/DataProvider";
import Table from "../components/Table";
// import Form from "../components/Form";

const OpportunityPage = () => {
    const API_URL = `${config.apiUrl}/opportunities/`;

    return <>
        <div className="container">
            <h2>Opportunities</h2>
            <DataProvider endpoint={API_URL} render={data => <Table data={data} />} />
            {/* <Form endpoint={API_URL} /> */}
        </div>
    </>
}

export { OpportunityPage };