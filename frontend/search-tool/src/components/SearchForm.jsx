import React from 'react'
import {useFormik} from "formik"
import * as Yup from "yup"

const formValidationSchema = Yup.object().shape({
    searchInput: Yup.string()
    .min(3, "Too Short")
    .required("search input is required")
});
export const SearchForm = () => {
    const {handleSubmit, handleBlur, handleChange, values, isSubmitting, isValidating, touched, errors} = useFormik({
        initialValues: {
            searchInput: "",
        },
        validationSchema: formValidationSchema,
        validateOnChange: true,
        onSubmit: values => {
            
          //validating before submit
          if(isValidating && isSubmitting){
            console.log("validating before submit")
            console.log("protect against double submit")
          }
          
          //dertermine if form is executed
          if(!isValidating && isSubmitting){
            console.log("form is submitting")
          }
            
        },
        validate: values => {
          
          let errors = {};
          if(!values.searchInput){
            errors.searchInput = "Required Input Search"
          }

          return errors

        }

    })


  return (
    <form onSubmit={handleSubmit}>
        <label htmlFor="searchInput">{errors && touched && <div>{errors.searchInput}</div>}</label>
        <input id="searchInput" placeholder="search here..." name="searchInput" type="text" onChange={handleChange} onBlur={handleBlur} value={values.searchInput}/>
        <button type="submit">search.</button>
    </form>
  )
}
