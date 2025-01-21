# Opensearch service
resource "aiven_opensearch" "opensearch" {
  project                 = var.project
  cloud_name              = var.cloud_name
  plan                    = var.plan
  service_name            = "opensearch"
  maintenance_window_dow  = "monday"
  maintenance_window_time = "10:00:00"
  opensearch_user_config {
      opensearch_version = "2"
  }
}

output "opensearch_service_uri" {
  value = aiven_opensearch.opensearch.service_uri
  sensitive = true
}

resource "docker_image" "python_image" {
  name    = "python-image"
  build {
    context = "./python"
  }
  triggers = {
    dir_sha1 = sha1(join("", [for f in fileset(path.module, "python/*") : filesha1(f)]))
  }
}

resource "docker_container" "python_container" {
  name  = "python-container"
  image = docker_image.python_image.name
  hostname = "python-container"
  
  command = [
    "python", "vectors.py", "--opensearch_url", aiven_opensearch.opensearch.service_uri
  ]

  depends_on = [docker_container.python_container, aiven_opensearch.opensearch]

  provisioner "local-exec" {
    command = "docker logs python-container"
  }
}