doc = {
    'info' : {
        'title' : 'API do Veroneze',
        'description' : 'An API that performs operations on a database',
        'contact' : {
            'email' : 'pedromartins12117@gmail.com',
        },
        'version' : '0.6.0',
    },
    'paths' : {
        '/login' : {
            'get' : {
                'description' : 'Returns access token',
                'summary' : 'Returns access token',
                'tags' : ['Authentication'],
                'responses' : {
                    '200' : {
                        'description' : 'ok',
                        'content' : {
                            'application/json' : {
                                'schema' : {
                                    '$ref' : '#/components/schemas/TokenGenerated'
                                }
                            }
                        }
                    },
                    '401' : {
                        'description' : 'error',
                        'content' : {
                            'application/json' : {
                                'schema' : {
                                    '$ref' : '#/components/schemas/ErrorModel'
                                }
                            }
                        }
                    }
                }
            },
            'parameters' : [
                {
                    'in' : 'query',
                    'name' : 'user',
                    'required' : True,
                    'schema' : {
                        'type' : 'string'
                    }
                },
                {
                    'in' : 'query',
                    'name' : 'password',
                    'required' : True,
                    'schema' : {
                        'type' : 'string'
                    }
                }
            ]            
        },
        '/aluno/{id}' : {
            'get' : {
                'description' : 'Returns the resource aluno of id=id',
                'summary' : 'Returns the resource aluno of id=id',
                'tags' : ['Aluno'],
                'security' : [
                    {
                        'bearerAuth' : [
                        ]
                    }
                ],
                'responses' : {
                    '200' : {
                        'description' : 'ok',
                        'content' : {
                            'application/json' : {
                                'schema' : {
                                    '$ref' : '#/components/schemas/Aluno'
                                }
                            }
                        }
                    },
                    '401' : {
                        'description' : 'error',
                        'content' : {
                            'application/json' : {
                                'schema' : {
                                    '$ref' : '#/components/schemas/ErrorModel'
                                }
                            }
                        }
                    },
                    '404' : {
                        'description' : 'error',
                        'content' : {
                            'application/json' : {
                                'schema' : {
                                    '$ref' : '#/components/schemas/ErrorModel'
                                }
                            }
                        }
                    },
                    '422' : {
                        'description' : 'error',
                        'content' : {
                            'application/json' : {
                                'schema' : {
                                    '$ref' : '#/components/schemas/ErrorModel'
                                }
                            }
                        }
                    }
                }
            },
            'put' : {
                'description' : 'Change a resource aluno in the database',
                'summary' : 'Change a resource aluno in the database',
                'tags' : ['Aluno'],
                'security' : [
                    {
                        'bearerAuth' : [
                        ]
                    }
                ],
                'responses' : {
                    '200' : {
                        'description' : 'ok',
                        'content' : {
                            'application/json' : {
                                'schema' : {
                                    '$ref' : '#/components/schemas/OkModel'
                                }
                            }
                        }
                    },
                    '400' : {
                        'description' : 'error',
                        'content' : {
                            'application/json' : {
                                'schema' : {
                                    '$ref' : '#/components/schemas/ErrorModel'
                                }
                            }
                        }
                    },                    
                    '401' : {
                        'description' : 'error',
                        'content' : {
                            'application/json' : {
                                'schema' : {
                                    '$ref' : '#/components/schemas/ErrorModel'
                                }
                            }
                        }
                    },                    
                    '404' : {
                        'description' : 'error',
                        'content' : {
                            'application/json' : {
                                'schema' : {
                                    '$ref' : '#/components/schemas/ErrorModel'
                                }
                            }
                        }
                    },
                    '422' : {
                        'description' : 'error',
                        'content' : {
                            'application/json' : {
                                'schema' : {
                                    '$ref' : '#/components/schemas/ErrorModel'
                                }
                            }
                        }
                    }
                },
                'requestBody' : {
                    'content' : {
                        'application/json' : {
                            'schema' : {
                                '$ref' : '#/components/schemas/Aluno'
                            },
                            'examples' : {
                                'Pedro 1' : {
                                    'description' : 'Pedro\'s example 1',
                                    'summary' : 'Pedro\'s example 1',
                                    'value' : {
                                        'id' : 103,
                                        'nome_completo' : 'Pedro de Souza',
                                        'endere??o' : {
                                            'numero' : '14',
                                        }
                                    }
                                },
                                'Pedro 2' : {
                                    'description' : 'Pedro\'s example 2',
                                    'summary' : 'Pedro\'s example 2',
                                    'value' : {
                                        'id' : 101,
                                        'endere??o' : {
                                            'cidade' : 'Catal??o'
                                        }
                                    }
                                }
                            }       
                        }
                    }
                }
            },
            'delete' : {
                'description' : 'Removes the resource aluno of id=id from the database',
                'summary' : 'Removes the resource aluno of id=id from the database',
                'tags' : ['Aluno'],
                'security' : [
                    {
                        'bearerAuth' : [
                        ]
                    }
                ],
                'responses' : {
                    '200' : {
                        'description' : 'ok',
                        'content' : {
                            'application/json' : {
                                'schema' : {
                                    '$ref' : '#/components/schemas/OkModel'
                                }
                            }
                        }
                    },
                    '401' : {
                        'description' : 'error',
                        'content' : {
                            'application/json' : {
                                'schema' : {
                                    '$ref' : '#/components/schemas/ErrorModel'
                                }
                            }
                        }
                    },
                    '404' : {
                        'description' : 'error',
                        'content' : {
                            'application/json' : {
                                'schema' : {
                                    '$ref' : '#/components/schemas/ErrorModel'
                                }
                            }
                        }
                    },
                    '422' : {
                        'description' : 'error',
                        'content' : {
                            'application/json' : {
                                'schema' : {
                                    '$ref' : '#/components/schemas/ErrorModel'
                                }
                            }
                        }
                    }
                }
            },
            'parameters' : [
                {
                    'in' : 'path',
                    'name' : 'id',
                    'required' : True,
                    'schema' : {
                        'type' : 'integer'
                    }
                }
            ]            
        },
        '/aluno' : {
            'post' : {
                'description' : 'Insert a resource aluno into the database',
                'summary' : 'Insert a resource aluno into the database',
                'tags' : ['Aluno'],
                'security' : [
                    {
                        'bearerAuth' : [
                        ]
                    }
                ],
                'responses' : {
                    '201' : {
                        'description' : 'ok',
                        'content' : {
                            'application/json' : {
                                'schema' : {
                                    '$ref' : '#/components/schemas/OkModel'
                                }
                            }
                        }
                    },
                    '400' : {
                        'description' : 'error',
                        'content' : {
                            'application/json' : {
                                'schema' : {
                                    '$ref' : '#/components/schemas/ErrorModel'
                                }
                            }
                        }
                    },
                    '401' : {
                        'description' : 'error',
                        'content' : {
                            'application/json' : {
                                'schema' : {
                                    '$ref' : '#/components/schemas/ErrorModel'
                                }
                            }
                        }
                    },
                    '422' : {
                        'description' : 'error',
                        'content' : {
                            'application/json' : {
                                'schema' : {
                                    '$ref' : '#/components/schemas/ErrorModel'
                                }
                            }
                        }
                    }
                },
                'requestBody' : {
                    'content' : {
                        'application/json' : {
                            'schema' : {
                                '$ref' : '#/components/schemas/Aluno'
                            },
                            'examples' : {
                                'Pedro' : {
                                    'summary' : 'Pedro\'s example',
                                    'description' : 'Pedro\'s example',
                                    'value' : {
                                        'id' : 102,
                                        'nome_completo' : 'Pedro Henrique Martins de Souza',
                                        'email' : 'pedrohms@discente.ufcat.edu.br',
                                        'endere??o' : {
                                            'rua' : '06',
                                            'numero' : 'N/A',
                                            'cidade' : 'Caldas Novas'
                                        },
                                        'curso' : 4,
                                        'disciplinas' : [
                                            'vibra????es mec??nicas',
                                            'l??gica digital',
                                            's?? fun????es'
                                        ]
                                    }
                                }
                            }
                        }
                    }
                }
            }   
        },
        '/aluno/page/{page_number}' : {
            'get' : {
                'description' : 'Returns the resources of type Aluno per page',
                'summary' : 'Returns the resources of type Aluno per page',
                'tags' : ['Aluno'],
                'security' : [
                    {
                        'bearerAuth' : [
                        ]
                    }
                ],
                'responses' : {
                    '200' : {
                        'description' : 'ok',
                        'content' : {
                            'application/json' : {
                                'schema' : {
                                    'type' : 'object',
                                    'properties' : {
                                        'alunos' : {
                                            'type' : 'array',
                                            'items' : {
                                                '$ref' : '#/components/schemas/Aluno'
                                            }
                                        }
                                    }
                                }
                            }
                        }
                    },
                    '401' : {
                        'description' : 'error',
                        'content' : {
                            'application/json' : {
                                'schema' : {
                                    '$ref' : '#/components/schemas/ErrorModel'
                                }
                            }
                        }
                    },
                    '404' : {
                        'description' : 'error',
                        'content' : {
                            'application/json' : {
                                'schema' : {
                                    '$ref' : '#/components/schemas/ErrorModel'
                                }
                            }
                        }
                    },
                    '422' : {
                        'description' : 'error',
                        'content' : {
                            'application/json' : {
                                'schema' : {
                                    '$ref' : '#/components/schemas/ErrorModel'
                                }
                            }
                        }
                    }
                },
                'parameters' : [
                    {
                        'in' : 'path',
                        'name' : 'page_number',
                        'required' : True,
                        'schema' : {
                            'type' : 'integer'
                        }
                    }
                ]
            }
        },
        '/curso/{id}' : {
            'get': {
                'description' : 'Returns the resource curso of id=id',
                'summary' : 'Returns the resource curso of id=id',
                'tags' : ['Curso'],
                'security' : [
                    {
                        'bearerAuth' : [
                        ]
                    }
                ],
                'responses' : {
                    '200' : {
                        'description' : 'ok',
                        'content' : {
                            'application/json' : {
                                'schema' : {
                                    '$ref' : '#/components/schemas/Curso'
                                }
                            }
                        }
                    },
                    '401' : {
                        'description' : 'error',
                        'content' : {
                            'application/json' : {
                                'schema' : {
                                    '$ref' : '#/components/schemas/ErrorModel'
                                }
                            }
                        }
                    },
                    '404' : {
                        'description' : 'error',
                        'content' : {
                            'application/json' : {
                                'schema' : {
                                    '$ref' : '#/components/schemas/ErrorModel'
                                }
                            }
                        }
                    },
                    '422' : {
                        'description' : 'error',
                        'content' : {
                            'application/json' : {
                                'schema' : {
                                    '$ref' : '#/components/schemas/ErrorModel'
                                }
                            }
                        }
                    }
                }
            },
            'put' : {
                'description' : 'Change a resource curso in the database',
                'summary' : 'Change a resource curso in the database',
                'tags' : ['Curso'],
                'security' : [
                    {
                        'bearerAuth' : [
                        ]
                    }
                ],
                'responses' : {
                    '200' : {
                        'description' : 'ok',
                        'content' : {
                            'application/json' : {
                                'schema' : {
                                    '$ref' : '#/components/schemas/OkModel'
                                }
                            }
                        }
                    },
                    '400' : {
                        'description' : 'error',
                        'content' : {
                            'application/json' : {
                                'schema' : {
                                    '$ref' : '#/components/schemas/ErrorModel'
                                }
                            }
                        }
                    },
                    '401' : {
                        'description' : 'error',
                        'content' : {
                            'application/json' : {
                                'schema' : {
                                    '$ref' : '#/components/schemas/ErrorModel'
                                }
                            }
                        }
                    },
                    '404' : {
                        'description' : 'error',
                        'content' : {
                            'application/json' : {
                                'schema' : {
                                    '$ref' : '#/components/schemas/ErrorModel'
                                }
                            }
                        }
                    },
                    '422' : {
                        'description' : 'error',
                        'content' : {
                            'application/json' : {
                                'schema' : {
                                    '$ref' : '#/components/schemas/ErrorModel'
                                }
                            }
                        }
                    }
                },
                'requestBody' : {
                    'content' : {
                        'application/json' : {
                            'schema' : {
                                '$ref' : '#/components/schemas/Curso'
                            },
                            'examples' : {
                                'matem??tica industrial' : {
                                    'description' : 'Example with matem??tica industrial',
                                    'summary' : 'Example with matem??tica industrial',
                                    'value' : {
                                        'id' : 5,
                                        'nome' : 'matem??tica insdustrial'
                                    }
                                }
                            }
                        }
                    }
                }
            },
            'delete' : {
                'description' : 'Removes the resource curso of id=id from the database',
                'summary' : 'Removes the resource curso of id=id from the database',
                'tags' : ['Curso'],
                'security' : [
                    {
                        'bearerAuth' : [
                        ]
                    }
                ],
                'responses' : {
                    '200' : {
                        'description' : 'ok',
                        'content' : {
                            'application/json' : {
                                'schema' : {
                                    '$ref' : '#/components/schemas/OkModel'
                                }
                            }
                        }
                    },
                    '401' : {
                        'description' : 'error',
                        'content' : {
                            'application/json' : {
                                'schema' : {
                                    '$ref' : '#/components/schemas/ErrorModel'
                                }
                            }
                        }
                    },
                    '404' : {
                        'description' : 'error',
                        'content' : {
                            'application/json' : {
                                'schema' : {
                                    '$ref' : '#/components/schemas/ErrorModel'
                                }
                            }
                        }
                    },
                    '422' : {
                        'description' : 'error',
                        'content' : {
                            'application/json' : {
                                'schema' : {
                                    '$ref' : '#/components/schemas/ErrorModel'
                                }
                            }
                        }
                    }
                }
            },
            'parameters': [
                {
                    'in' : 'path',
                    'name' : 'id',
                    'required' : True,
                    'schema' : {
                        'type' : 'integer'
                    }
                }
            ]
        },
        '/curso' : {
            'post' : {
                'description' : 'Insert a resource curso into the database',
                'summary' : 'Insert a resource curso into the database',
                'tags' : ['Curso'],
                'security' : [
                    {
                        'bearerAuth' : [
                        ]
                    }
                ],
                'responses' : {
                    '201' : {
                        'description' : 'ok',
                        'content' : {
                            'application/json' : {
                                'schema' : {
                                    '$ref' : '#/components/schemas/OkModel'
                                }
                            }
                        }
                    },
                    '400' : {
                        'description' : 'error',
                        'content' : {
                            'application/json' : {
                                'schema' : {
                                    '$ref' : '#/components/schemas/ErrorModel'
                                }
                            }
                        }
                    },
                    '401' : {
                        'description' : 'error',
                        'content' : {
                            'application/json' : {
                                'schema' : {
                                    '$ref' : '#/components/schemas/ErrorModel'
                                }
                            }
                        }
                    },
                    '422' : {
                        'description' : 'error',
                        'content' : {
                            'application/json' : {
                                'schema' : {
                                    '$ref' : '#/components/schemas/ErrorModel'
                                }
                            }
                        }
                    }
                },
                'requestBody' : {
                    'content' : {
                        'application/json' : {
                            'schema' : {
                                '$ref' : '#/components/schemas/Curso'
                            },
                            'examples' : {
                                'matem??tica industrial' : {
                                    'summary' : 'Example with matem??tica industrial',
                                    'description' : 'Example with matem??tica industrial',
                                    'value' : {
                                        'id' : 5,
                                        'nome' : 'matematica industrial'
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    },
    'components' : {
        'schemas' : {
            'Aluno' : {
                'type': 'object',
                'properties' : {
                    'id' : {
                        'type' : 'integer',
                    },
                    'nome_completo' : {
                        'type' : 'string'
                    },
                    'email' : {
                        'type' : 'string'
                    },                    
                    'endere??o' : {
                        'type' : 'object',
                        'properties' : {
                            'rua' : {
                                'type' : 'string',
                            },
                            'numero' : {
                                'type' : 'string',
                            },
                            'cidade' : {
                                'type' : 'string'
                            }
                        }
                    },
                    'curso' : {
                        'type' : 'integer'
                    },
                    'disciplinas' : {
                        'type' : 'array',
                        'items' : {
                            'type' : 'string',
                        }
                    }
                }
            },
            'Curso' : {
                'type' : 'object',
                'properties' : {
                    'id' : {
                        'type' : 'integer'
                    },
                    'nome' : {
                        'type' : 'string'
                    }
                }
            },
            'ErrorModel' : {
                'type' : 'object',
                'properties' : {
                    'error' : {
                        'type' : 'object',
                        'properties' : {
                            'status' : {
                                'type' : 'integer'
                            },
                            'message' : {
                                'type' : 'string'
                            }
                        }
                    }
                }
            },
            'OkModel' : {
                'type' : 'object',
                'properties' : {
                    'ok' : {
                        'type' : 'object',
                        'properties' : {
                            'status' : {
                                'type' : 'integer'
                            },
                            'message' : {
                                'type' : 'string'
                            }
                        }
                    }
                }
            },
            'TokenGenerated' : {
                'type' : 'object',
                'properties' : {
                    'ok' : {
                        'type' : 'object',
                        'properties' : {
                            'status' : {
                                'type' : 'integer'
                            },
                            'message' : {
                                'type' : 'string'
                            },
                            'access_token' : {
                                'type' : 'string'
                            }
                        }
                    }
                }
            }
        },
        'securitySchemes' : {
            'bearerAuth' : {
                'type' : 'http',
                'scheme' : 'bearer',
                'bearerFormat' : 'JWT'
            }
        }
    },
    'tags' : [
        {
            'name' : 'Authentication',
            'description' : 'Routes for authentication'
        },
        {
            'name' : 'Aluno',
            'description' : 'Resource Aluno'
        },
        {
            'name' : 'Curso',
            'description' : 'Resource Curso'
        }
    ]
}
