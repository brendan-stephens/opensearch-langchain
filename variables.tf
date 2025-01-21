variable "project" {
    description = "A name for identifying grouped services"
    default = "sa-sandbox"
}

variable "cloud_name" {
    description = "The cloud where service will be created"
    default = "google-us-east1"
}

variable "plan" {
    description = "The plan to use for deployment"
    default = "business-4"
}

variable "aiven_api_token" {
    description = "The api token for the environment prod or dev"
    default = ""
}

