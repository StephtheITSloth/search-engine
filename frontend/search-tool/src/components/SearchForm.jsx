import React, {useState} from 'react'
import {useFormik} from "formik"
import * as Yup from "yup"
import {useQuery} from '@tanstack/react-query'
import { axiosInstance } from '../axiosInstance'

const searchFormValidationSchema = Yup.object().shape({
    searchInput: Yup.string()
    .min(3, ('Too Short - input should have more than 3 characters'))
    .max(25, ('Too Long'))
    .required('Input is Required')
})

async function fetchData(){
    const {data} = await axiosInstance.get()
    return data
}


function SearchForm() {
    const [searchData, setSearchData] = useState([])

    const fallback = []

    const {data = fallback, isLoading} = useQuery({
    queryKey: ['search'],
    queryFn: fetchData
    });

    const {values, handleBlur, handleChange, handleSubmit, errors, touched, isSubmitting, isValidating} = useFormik({
        initialValues: {
            searchInput: ""
        },
        validationSchema: searchFormValidationSchema,
        validateOnChange: true,
        onSubmit: async (values) => {
            await fetchData()
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
    <>
        <form onSubmit={handleSubmit}>
            <label htmlFor="searchInput">{errors.searchInput && <div>{errors.searchInput}</div>}</label>
            <input type="text" placeholder="Enter your search value" onChange={handleChange}
                onBlur={handleBlur}
                value={values.searchInput}
                name="searchInput"/>
            <button type="submit">search</button>
        </form>
        {isLoading && (<h3>Loading...</h3>)}
        {data.map(elem => {<p key={elem.id}>{elem.title}</p>})}
    </>
  )
}

export default SearchForm