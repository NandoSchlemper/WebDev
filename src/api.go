package main

import (
	"log"
	"net/http"
)

func main() {
	resp, err := http.Get("https://gobyexample.com")
	if err != nil {
		log.Fatalln("Deu pau", err)
	}

	log.Println("Response status:", resp.Status)
}
