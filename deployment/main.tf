provider "google" {
  project = "aide-final-project"
  region  = "us-central1"
}

# 1. Tạo cụm Kubernetes (GKE)
resource "google_container_cluster" "primary" {
  name     = "aide-final-cluster"
  location = "us-central1-a"  
  deletion_protection = false
  
  # Cấu hình tối thiểu để tiết kiệm chi phí
  initial_node_count = 3

  node_config {
    machine_type = "e2-medium" # Cấu hình vừa đủ để chạy KServe/MLFlow
    disk_size_gb = 30
  }
}

# 2. Xuất tên cụm sau khi tạo xong
output "kubernetes_cluster_name" {
  value = google_container_cluster.primary.name
}