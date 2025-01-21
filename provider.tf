terraform {
  required_providers {
    aiven = {
      source = "aiven/aiven"
      version = ">= 4.0.0, < 5.0.0"
    }  
    docker = {
      source  = "kreuzwerker/docker"
      version = ">=3.0.0"
    }
  }
}

provider "aiven" {
  api_token = var.aiven_api_token
}

provider "docker" {
  # If you want to use a remote Docker/Podman daemon, you can specify the host here
  # host = "unix:///var/run/docker.sock"
}
