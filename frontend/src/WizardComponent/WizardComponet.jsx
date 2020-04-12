import React,{ Fragment, useState, useEffect } from 'react';
import Button from 'react-bootstrap/Button';
import { Grid, Row, Col} from 'react-bootstrap';
import Table from "../components/Table";
import StepWizard from 'react-step-wizard';

const WizardComponent = () => {
  const [state, updateState] = useState({
       form: {}
   });
   const updateForm = (key, value) => {
       const { form } = state;

       form[key] = value;
       updateState({
           ...state,
           form,
       });
   };
   const onStepChange = (stats) => {
      // console.log(stats);
  };

  const setInstance = SW => updateState({
      ...state,
      SW,
  });

  const { SW, demo } = state;
   return (
        <div className='container'>
            <h3>Wizard Oportunidad</h3>
            <div className={'jumbotron'}>
                <div className='row'>
                    <div className={`col-12 col-sm-6 offset-sm-3 `}>
                        <StepWizard
                            onStepChange={onStepChange}
                            isHashEnabled
                            //nav={<Nav />}
                            instance={setInstance}
                        >
                            <First hashKey={'FirstStep'} update={updateForm} />
                            <Second form={state.form} />
                            <Third />
                            <Fourth />
                        </StepWizard>
                    </div>
                </div>
            </div>
            //{ (demo && SW) && <InstanceDemo SW={SW} /> }
        </div>
    );
};


/** Stats */
const Stats = ({
    currentStep,
    firstStep,
    goToStep,
    lastStep,
    nextStep,
    previousStep,
    totalSteps,
    step,
}) => (
    <div>
        <hr />
        {
            <button className='btn btn-default btn-block' onClick={previousStep}>Go Back</button>
        }
        { step < totalSteps ?
            <button className='btn btn-primary btn-block' onClick={nextStep}>Continue</button>
            :
            <button className='btn btn-success btn-block' onClick={nextStep}>Finish</button>
        }
        <hr />
        <div style={{ fontSize: '21px', fontWeight: '200' }}>
            <h4>Other Functions</h4>
            <div>Paso Actual: {currentStep}</div>
            <div>Pasos Finales: {totalSteps}</div>
        </div>
    </div>
);




/** Steps */

const First = props => {
    const update = (e) => {
        props.update(e.target.name, e.target.value);
    };

    return (
      <div>
            <h3 className='text-center'>Nueva Oportunidad</h3>
        <form>
            <label>Datos Clientes</label>
            <input type='text' className='form-control' name='clientName' placeholder='Nombre Cliente'
             onChange={update} />
            <input type='url' className='form-control' name='clientUrl' placeholder='Url'
             onChange={update} />
            <input type='email' className='form-control' name='clientEmail' placeholder='Email'
             onChange={update} />
            <input type='text' className='form-control' name='extraData' placeholder='Data extra'
             onChange={update} />
            <Stats step={1} {...props} />
        </form>
      </div>
    );
};

const Second = props => {
  return (
  <div>
    <form>
      <fieldset>
         <h3 className='text-center'>Modalidades de Trabajo</h3>
         <input type="radio" value="" name="gender"/> Fix-Price
         < input type="radio" value="" name="gender"/> Staff augmentation
         <input type="radio" value="FEMALE" name="gender"/> No definido
     </fieldset>
    </form>
      <div>
         <input type="checkbox" {...props} /> Ingles excluyente
      </div>
      <Stats step={1} {...props} />
</div>

      );
 }


const perfil_tecnologia =[
    {
        "Cantidad": "2",
        "Tecnologia": "Java",
        "Seniority":"Junior"
    },
    {
        "Cantidad": "1",
        "Tecnologia": "PHP",
        "Seniority":"Semi-Senior"
    },
    {
        "Cantidad": "4",
        "Tecnologia": "React",
        "Seniority":"Ninja"
    }
]


const Third = props => {
   return (
       <div>
           <h2 >Crear Perfil</h2>
           <h4 >Tecnologias</h4>
           <select>
                 <option value="Python">Python</option>
                 <option value="Java">Java</option>
                 <option selected value="JS">Javascript</option>
                 <option value="PHP">Php</option>
               </select>

               <select>
                     <option value="Junior">Junior</option>
                     <option value="Semi-Senior">Semi-Senior</option>
                     <option selected value="Senior">Senior</option>
                     <option value="Ninja">Php</option>
                   </select>
            <Button variant="success">Agregar tecnologia</Button>{' '}
            <div>
                  <Table data={perfil_tecnologia} />
            </div>
            <Button variant="primary">Aceptar</Button>{' '}
           <Stats step={1} {...props} />
       </div>
  );
}

  const perfil_cooperativa =[
      {
          "Cooperativa": "Camba",
          "Estado": "Regular"

      },

      {
        "Cooperativa": "Fiqus",
        "Estado": "Normal"
      }
  ]

const Fourth= props => {
      return (
          // <Grid>
          //   <h3 className='text-center'>Nueva Oportunidad</h3>
          //   <Row>
          //       <Col md={4}>
          <div>
                    <form>
                        <h4>Datos finales </h4>
                        <label>Costo Proyecto</label>
                        <input type='text' className='form-control' name='clientName' placeholder='Costo Proyecto'
                          />
                         <label>Informacion Adicional</label>
                        <input type='text' className='form-control' name='clientUrl' placeholder='Info_adicional'
                          />
                         <label>Fecha Limite</label>
                        <input type='date' className='form-control' name='clientEmail' placeholder='fecha_limite'
                          />
                    </form>
                    <div>
                          <Table data={perfil_cooperativa} />
                    </div>
          </div>
          //       </Col>
          //       <Col md={8}>
          //               <h4>Cooperativa Aplican </h4>
          //             <Table data={perfil_cooperativa} />
          //       </Col>
          //   <Row>
          //   <Stats step={1} {...props} />
          // <Grid>
  );
}
export { WizardComponent };
