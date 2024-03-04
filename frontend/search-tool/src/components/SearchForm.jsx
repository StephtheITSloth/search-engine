import React, {useState} from 'react'
import { useFormik } from "formik"
import * as Yup from "yup"
import ExportCSV from "./ExportCSV"
import { ExportReactCSV } from './ExportReactCSV'



const searchFormValidationSchema = Yup.object().shape({
    doctorId: Yup.string()
    .min(3, ('Too Short - input should have more than 3 characters'))
    .max(25, ('Too Long'))
    .required('Input is Required')
})



function SearchForm() {
    const [jsonData, setJsonData] = useState('');


    const {values, handleBlur, handleChange, handleSubmit, errors, touched, isSubmitting, isValidating} = useFormik({
        initialValues: {
            doctorId: ""
        },
        validationSchema: searchFormValidationSchema,
        validateOnChange: true,
        onSubmit: async (values) => {
            try {
                const response = await fetch(`http://127.0.0.1:5000/api/v1/payments?doctorId=${values.doctorId}`);
                const data = await response.json();
                console.log(data)
                setJsonData(data);
            } catch (error) {
                console.log(error.message)
            }
        },
        validate: values => {
            let errors = {}
            if(!values.doctorId){
                errors.doctorId = "Search input should have at least 3 characters"
            }

            return errors
        }
    })
  return (
    <>
        <form onSubmit={handleSubmit}>
            <label htmlFor="doctorId">{errors.doctorId && <div>{errors.doctorId}</div>}</label>
            <input type="text" placeholder="Enter your search value" onChange={handleChange}
                onBlur={handleBlur}
                value={values.doctorId}
                name="doctorId"/>
            <button type="submit">search</button>
        </form>
        {jsonData && <ExportCSV csvData={jsonData} fileName={"search data"}/>}
        {jsonData && (<div>
            <ExportReactCSV csvData={Object.keys(jsonData).map(key => jsonData[key])} fileName={"search data"} />
        </div>)}
    </>
  )
}

export default SearchForm
