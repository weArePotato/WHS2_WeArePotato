A web application for managing user experiments for Mozilla Firefox. 

VSCode setup

    If using VSCode, configure workspace folders
        Add /experimenter/ and /experimenter/app folders to your workspace (File -> Add Folder to Workspace -> path/to/experimenter/app)
        From the /experimenter/app folder, run yarn install

            Make sure you are using the correct version of node

            node -v

            Troubleshooting:
                Changing node version
                Clear npm cache: npm cache clean --force

Google Cloud Bucket for Media Storage

We support user uploads of media (e.g. screenshots) for some features.

In local development, the default is to store these files in /app/media using Django's FileSystemStorage class and the MEDIA_ROOT and MEDIA_URL settings.

In production, a GCP bucket and credentials are required.

The bucket name is configured with the UPLOADS_GS_BUCKET_NAME setting. For example:

UPLOADS_GS_BUCKET_NAME=nimbus-experimenter-media-dev-uploads

For local testing of a production-like environment, The credentials should be configured as described in the previous section on Google Credentials for Jetstream.

In the real production deployment, credentials are configured via workload identity in Google Kubernetes Engine.
