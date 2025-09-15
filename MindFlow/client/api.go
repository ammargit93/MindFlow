package main

import (
	"io"
	"net/http"
	"net/url"
)

func SendQuery(query string) string {
	encoded := url.QueryEscape(query)
	url := "http://localhost:8000/mindflow/api/?query=" + encoded

	// disable keep-alive just to avoid FastAPI warnings
	transport := &http.Transport{DisableKeepAlives: true}
	client := &http.Client{Transport: transport}

	resp, err := client.Get(url)
	if err != nil {
		panic(err)
	}
	defer resp.Body.Close()

	body, err := io.ReadAll(resp.Body)
	if err != nil {
		panic(err)
	}

	return string(body)
}
