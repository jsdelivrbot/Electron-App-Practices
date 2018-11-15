import axios from 'axios';


const API_KEY = "7fae8263f88d0723b380333043a71543";
const ROOT_URL = `https://api.openweathermap.org/data/2.5/forecast?appid=${API_KEY}`;


export const FETCH_WEATHER = 'FETCH_WEATHER';


export function fetchWeather(city){
    const url = `${ROOT_URL}&q=${city},bd`;
    const request = axios.get(url);

    //console.log('Request :', request);

    return {
        type: FETCH_WEATHER,
        payload : request
    };

}