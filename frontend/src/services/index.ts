import axios, { AxiosInstance, AxiosRequestConfig } from "axios";
import { BASE_URL } from "../constants";

export const client: AxiosInstance = axios.create({
  baseURL: BASE_URL,
} as AxiosRequestConfig);

