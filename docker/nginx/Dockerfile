FROM node:10
RUN npm install yarn
ADD frontend/package.json /srv/ui/package.json
WORKDIR /srv/ui
RUN yarn install --allow-root --unsafe-perm=true
ADD frontend/. /srv/ui
RUN yarn build

FROM nginx:latest
WORKDIR /usr/share/nginx/html
COPY --from=0 /srv/ui/dist .
COPY docker/nginx/api-endpoint.conf /etc/nginx/conf.d/.
RUN mkdir -p /srv/back/static
RUN chown -R nginx:www-data /srv/back/static
