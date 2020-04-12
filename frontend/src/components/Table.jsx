import React from "react";
import PropTypes from "prop-types";
import key from "weak-key";

const Table = ({ data }) =>
  !data.length ? null : (
    <div className="column">
      <table className="table is-striped">
        <thead>
          <tr>
            {Object.entries(data[0]).map(el => <th key={key(el)}>{el[0]}</th>)}
          </tr>
        </thead>
        <tbody>
          {data.map(el => (
            <tr key={el.id}>
              {Object.entries(el).map(el => <td key={key(el)}>{el[1]}</td>)}
            </tr>
          ))}
        </tbody>
      </table>
      <p className="subtitle">
        <strong>{data.length}</strong> items
      </p>
    </div>
  );

Table.propTypes = {
  data: PropTypes.array.isRequired
};

export default Table;