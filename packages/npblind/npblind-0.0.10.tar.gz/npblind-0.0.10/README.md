# npblind
A package to manage BigQuery policy tag and GCP IAM related tasks

Reference:
- [GCP roles](https://github.com/ecneladis/gcp_managed_roles/blob/master/gcp-roles.json)
- [GCP roles](https://cloud.google.com/iam/docs/understanding-roles)
- [GCP roles predefined](https://codehex.dev/gcp_predefined_roles/)
- https://github.com/googleapis/python-dlp/tree/main/samples/generated_samples
- https://github.com/GoogleCloudPlatform/python-docs-samples/tree/main/dlp/snippets
- https://github.com/googleapis/python-bigquery-datapolicies
- https://cloud.google.com/python/docs/reference/datacatalog/latest/google.cloud.datacatalog_v1.services.policy_tag_manager.PolicyTagManagerClient


Workaround:
- https://cloud.google.com/sdk/gcloud/reference/data-catalog/taxonomies
  - Untested: `gcloud data-catalog taxonomies policy-tags set-iam-policy POLICY_TAG --location=LOCATION --taxonomy=TAXONOMY policy.json`
  - Tested & Works:
  ```bash
  # one by one: works !!!
  gcloud beta data-catalog taxonomies policy-tags \
      add-iam-policy-binding projects/nplearn/locations/asia-southeast1/taxonomies/7979849403702726703/policyTags/6110705995628818296 \
      --location='asia-southeast1' \
      --taxonomy='7979849403702726703' \
      --member='user:nplearn.channel@gmail.com' \
      --role='roles/datacatalog.categoryFineGrainedReader'


  # using file: not working
  gcloud data-catalog taxonomies policy-tags \
      set-iam-policy projects/nplearn/locations/asia-southeast1/taxonomies/7979849403702726703/policyTags/6110705995628818296 \
      --location=asia-southeast1 \
      --taxonomy=7979849403702726703 policytag.yaml

  # get policy
  gcloud beta data-catalog taxonomies policy-tags \
      get-iam-policy projects/nplearn/locations/asia-southeast1/taxonomies/7979849403702726703/policyTags/6110705995628818296 \
      --location='asia-southeast1' \
      --taxonomy='7979849403702726703'


  # describe
  gcloud beta data-catalog taxonomies policy-tags \
      describe projects/nplearn/locations/asia-southeast1/taxonomies/7979849403702726703/policyTags/6110705995628818296 \
      --location='asia-southeast1' \
      --taxonomy='7979849403702726703'

  # list
  gcloud beta data-catalog taxonomies policy-tags \
      list \
      --location='asia-southeast1' \
      --taxonomy='7979849403702726703'
  ```
