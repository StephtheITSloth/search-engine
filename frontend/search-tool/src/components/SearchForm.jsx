import React from 'react'
import {useFormik} from "formik"
import * as Yup from "yup"

const searchFormValidationSchema = Yup.object().shape({
    searchInput: Yup.string()
    .min(3, ('Too Short - input should have more than 3 characters'))
    .max(25, ('Too Long'))
    .required('Input is Required')
})

function SearchForm() {
    const {values, handleBlur, handleChange, handleSubmit, errors, touched, isSubmitting, isValidating} = useFormik({
        initialValues: {
            searchInput: ""
        },
        validationSchema: searchFormValidationSchema,
        validateOnChange: true,
        onSubmit: values => {

            // //guard for validation
            // if(isValidating && isSubmitting){
            //     console.log("is Valid")
            // }

            console.log("is valid")

        },
        validate: values => {
            let errors = {}
            if(!values.searchInput){
                errors.searchInput = "Search input should have at least 3 characters"
            }

            return errors
        }
    })
  return (
    <form onSubmit={handleSubmit}>
        <label htmlFor="searchInput">{errors.searchInput && <div>{errors.searchInput}</div>}</label>
        <input type="text" placeholder="Enter your search value" onChange={handleChange}
             onBlur={handleBlur}
             value={values.searchInput}
             name="searchInput"/>
        <button type="submit">search</button>
    </form>
  )
}

export default SearchForm