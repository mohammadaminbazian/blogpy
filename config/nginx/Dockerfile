FROM nginx:latest
LABEL MANINTAINER="Mohammad Bazian"

COPY nginx.conf /ect/nginx/conf.d/default.conf
EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]