'use strict';

const env = {
  PORT: process.env.PORT || 8080,
  DATABASE_NAME: process.env.DATABASE_NAME || 'somedb',
  DATABASE_HOST: process.env.DATABASE_HOST ||"http://10.110.9.61",
  DATABASE_USERNAME: process.env.DATABASE_USERNAME || 'docker',
  DATABASE_PASSWORD: process.env.DATABASE_PASSWORD || 'docker',
  DATABASE_PORT: process.env.DATABASE_PORT || 30093,
  DATABASE_DIALECT: process.env.DATABASE_DIALECT || 'postgres',

  NODE_ENV: process.env.NODE_ENV || 'development'
};

module.exports = env;
