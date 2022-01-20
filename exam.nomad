job "http-service" {
  datacenters = ["dc1"]

  

  group "echo" {
    count = 1

    task "server" {
      driver = "docker"
      config {
        image = "gowri45/vasu_2511:latest"
        args = [
          "-listen", ":8080",
	  "-text", "Hello world from IP:${NOMAD_IP_http} and on port:${NOMAD_PORT_http}",
        ]
      }
resources{
network{
mbits = 10
port "http"{}
}
}
}
}
}
